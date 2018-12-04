from page_creator import save_page, save_page_about
from datetime import datetime as dt
from horoscope import generate_prophecies
from data import horoscope_data


today = dt.now().date()
save_page(
    title="Гороскоп на сегодня",
    # header="Что день " + str(today) + " готовит.",
    header="Ваши предсказания на " + str(today),
    paragraphs=generate_prophecies(),
)

save_page_about(
    title="О реализации",
    header="О чем все это",
    data=horoscope_data,
)
