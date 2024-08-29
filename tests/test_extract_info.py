from core.extract_info import extract_client_info


def test_extract_client_info(client_text):
    expected_output = [
        ("João Silva", "20"),
        ("Maria Souza", "15"),
        ("Marina Oliveira", "1"),
    ]

    results = extract_client_info(client_text, is_filename=False)
    assert results == expected_output


def test_extract_client_info_with_no_matches():
    no_match_text = """
    This text does not contain any valid client information.
    """
    results = extract_client_info(no_match_text, is_filename=False)
    assert results == []
