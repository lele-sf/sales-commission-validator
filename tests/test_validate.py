from core.validate import validate_payments


def test_validate(sales_data, payment_data):
    expected_results = [
        {
            "Nome do Vendedor": "Maria Oliveira",
            "Valor Incorreto": 100.0,
            "Valor Correto": 40.0,
        },
        {
            "Nome do Vendedor": "Pedro Souza",
            "Valor Incorreto": 400.0,
            "Valor Correto": 200.0,
        },
    ]

    results = validate_payments(sales_data, payment_data)
    assert results == expected_results


def test_validate_empty_data():
    sales_data = []
    payment_data = []

    results = validate_payments(sales_data, payment_data)
    assert results == []


def test_validate_with_missing_keys(sales_data):
    invalid_payment_data = [
        {
            "Data do Pagamento": "2023-12-15",
            "Nome do Vendedor": "João Silva",
        }
    ]

    results = validate_payments(sales_data, invalid_payment_data)
    assert results == []
