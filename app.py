import sys # System-specific parameters and functions
import easyocr as ocr  # OCR
import streamlit as st  # web app
from streamlit import cli as stcli # cli web app
from PIL import Image  # opening images
import numpy as np  # for array conversions


st.set_page_config(
    page_title="Распознавание",
    page_icon="🔍",
    layout="wide",
    menu_items={
         'Get Help': None,
         'Report a bug': None,
         
         'About': "# Распознавание текста на 83 языках мира. Создано в России, студентом СРКВТиЭ, группа 41/1, Богославцев Данила."
    }
)


@st.cache
def load_model(lang):
    return ocr.Reader([lang], model_storage_directory=".")


def main():
    st.title("🔍Распознавание текста с изображения")
    st.write("Для оптического распознавания символов необходимо выбрать из списка в левой части язык соответсующий языку текста")
    image = st.file_uploader(
        label="Загрузить изображение", type=["png", "jpg", "jpeg"]
    )


    langs = {
        "Абазинский": "abq",
        "Адыгейский": "ady",
        "Африкаанс": "af",
        "Ангика": "ang",
        "Арабский": "ar",
        "Ассамский": "as",
        "Аварский": "ava",
        "Азербайджанский": "az",
        "Белорусский": "be",
        "Болгарский": "bg",
        "Бихарский": "bh",
        "Бходжпури": "bho",
        "Бенгальский": "bn",
        "Боснийский": "bs",
        "Упрощенный Китайский": "ch_sim",
        "Традиционный Китайский": "ch_tra",
        "Чеченский": "che",
        "Чешский": "cs",
        "Валлийский": "cy",
        "Датский": "da",
        "Даргинский": "dar",
        "Немецкий": "de",
        "Английский": "en",
        "Испанский": "es",
        "Эстонский": "et",
        "Персидский": "fa",
        "Французский": "fr",
        "Ирландский": "ga",
        "Конкани": "gom",
        "Хинди": "hi",
        "Хорватский": "hr",
        "Венгерский": "hu",
        "Индонезийский": "id",
        "Ингушский": "inh",
        "Исландский": "is",
        "Итальянский": "it",
        "Японский": "ja",
        "Кабардино-черкесский": "kbd",
        "Каннада": "kn",
        "Корейский": "ko",
        "Курдский": "ku",
        "Латинский": "la",
        "Лакский": "lbe",
        "Лезгинский": "lez",
        "Литовский ": "lt",
        "Латышский": "lv",
        "Магахи": "mah",
        "Майтхили": "mai",
        "Маори": "mi",
        "Монгольский": "mn",
        "Маратхи": "mr",
        "Малайский": "ms",
        "Мальтийский": "mt",
        "Непальский": "ne",
        "Неварский": "new",
        "Нидерландский": "nl",
        "Норвежский": "no",
        "Окситанский": "oc",
        "Пали": "pi",
        "Польский": "pl",
        "Португальский": "pt",
        "Румынский": "ro",
        "Русский ": "ru",
        "Сербский (кириллица)": "rs_cyrillic",
        "Сербский (латиница)": "rs_latin",
        "Садри (Нагпури)": "sck",
        "Словацкий": "sk",
        "Словенский": "sl",
        "Албанский": "sq",
        "Шведский": "sv",
        "Суахили": "sw",
        "Тамильский": "ta",
        "Табасаранский": "tab",
        "Телугу": "te",
        "Тайский": "th",
        "Таджикский": "tjk",
        "Тагальский": "tl",
        "Турецкий": "tr",
        "Уйгурский": "ug",
        "Украинский": "uk",
        "Урду": "ur",
        "Узбекский": "uz",
        "Вьетнамский": "vi",
    }


    label_langs = st.sidebar.title('📝🗺️Выбор языка')
    feature_choice = st.sidebar.selectbox(
        "Укажите язык текста для распознавания ", list(langs.keys())
    )


    info_text = st.sidebar.text('Доступно 83 языка')
    if image is not None:
        input_image = Image.open(image)
        st.image(input_image)
        reader = load_model(lang=langs.get(feature_choice))
        with st.spinner("🤖 Распознавание... "):
            result = reader.readtext(
                np.array(input_image)
            )
            out_str = " "
            list_text = [ftext[1] for ftext in result]
            st.title("Загрузка результата:")
            with open(".txt", 'w') as file:
                file.write(out_str.join(list_text))
            result_file = open(".txt", 'r')
            st.download_button('Скачать распознанный текст', result_file)

            st.title("Распознанное изображение в виде текста:")

  
            futext = st.write(out_str.join(list_text))
            st.title("Распознанное изображение в списке:")
            result_text = [text[1] for text in result]
            st.write(result_text)
    else:
        st.info(
            "Пожалуйста, выберете язык и загрузите изображение для распознавания..."
        )
    st.caption("Made in Russia with ❤️ by Bogoslavtsev")


if __name__ == "__main__":
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
