def entrada_valida(texto: str) -> bool:
    """
    Valida a entrada do usuário:
    - Retorna False se for vazia ou apenas espaços.
    - Retorna True se for uma entrada válida.
    """
    if not texto:
        return False
    if texto.strip() == "":
        return False
    return True