def ordinal(num : int) -> str:
    """
    Return the ordinal of a number \n
    For example, 1 -> 1st , 13 -> 13th , 22 -> 22rd
    """
    remainder = num % 100
    if remainder in (11, 12, 13):
        return str(num) + "th"
    else:
        suffixes = ["th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th"]
        return str(num) + suffixes[num % 10]

