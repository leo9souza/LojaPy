def formata_float_moeda(valor: float) -> str:
    """Formata um valor float como moeda (R$).
    Args:
        valor (float): O valor a ser formatado.

    Returns:
        str: O valor formatado como moeda.
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")