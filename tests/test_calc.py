from core.calc import calculate_commission


def test_calc(sales_data):
    expected_results = [
        {
            "Nome do Vendedor": "João Silva",
            "Comissão Inicial": 100.0,
            "Comissão Final": 100.0,
        },
        {
            "Nome do Vendedor": "Maria Oliveira",
            "Comissão Inicial": 50.0,
            "Comissão Final": 40.0,
        },
        {
            "Nome do Vendedor": "Pedro Souza",
            "Comissão Inicial": 200.0,
            "Comissão Final": 200.0,
        },
    ]

    results = calculate_commission(sales_data)
    assert results == expected_results


def test_calc_empty_data():
    sales_data = []

    results = calculate_commission(sales_data)
    assert results == []


def test_calc_with_missing_keys():
    sales_data = [
        {
            "Nome do Vendedor": "João Silva",
            "Canal de Venda": "Online",
        }
    ]
    results = calculate_commission(sales_data)
    assert results == []


def test_calc_with_high_commission():
    sales_data = [
        {
            "Nome do Vendedor": "Ana Paula",
            "Valor da Venda": "R$ 20000,00",
            "Canal de Venda": "Offline",
        }
    ]
    expected_results = [
        {
            "Nome do Vendedor": "Ana Paula",
            "Comissão Inicial": 2000.0,
            "Comissão Final": 1800.0,
        }
    ]
    results = calculate_commission(sales_data)
    assert results == expected_results
