from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transaction):
    transaction_filter = filter_by_currency(transaction, "USD")
    assert next(transaction_filter)["id"] == 939719570
    assert next(transaction_filter)["id"] == 142264268
    assert next(transaction_filter)["id"] == 895315941


def test_transaction_descriptions(transaction):
    descriptions_generator = transaction_descriptions(transaction)
    assert next(descriptions_generator) == "Перевод организации"
    assert next(descriptions_generator) == "Перевод со счета на счет"
    assert next(descriptions_generator) == "Перевод со счета на счет"
    assert next(descriptions_generator) == "Перевод с карты на карту"
    assert next(descriptions_generator) == "Перевод организации"


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
