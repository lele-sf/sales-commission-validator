from core.handle_data import parse_value


def calculate_commission(sales_data):
    results = []
    try:
        for sale in sales_data:
            sale_value = parse_value(sale["Valor da Venda"])
            initial_commission = sale_value * 0.10
            final_commission = initial_commission

            if sale["Canal de Venda"] == "Online":
                marketing_commission = initial_commission * 0.20
                final_commission -= marketing_commission

            if final_commission >= 1500:
                manager_commission = final_commission * 0.10
                final_commission -= manager_commission

            results.append(
                {
                    "Nome do Vendedor": sale["Nome do Vendedor"],
                    "Comissão Inicial": initial_commission,
                    "Comissão Final": final_commission,
                }
            )
    except Exception as e:
        print(f"Error calculating commission: {e}")
        return []
    return results
