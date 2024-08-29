import re


def extract_client_info(source, is_filename=True):
    try:
        if is_filename:
            with open(source, "r", encoding="utf-8") as file:
                text = file.read()
        else:
            text = source

        regex = r"\d+\.\s+([A-Za-zÀ-ÖØ-öø-ÿ\s]+),.*?detentora? de (\d+) cotas?\."
        resultados = re.findall(regex, text)
        return resultados
    except Exception as e:
        print(f"Error extracting client info: {e}")
        return []
