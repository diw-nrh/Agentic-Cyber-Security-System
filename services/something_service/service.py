def get_something(something: str, number: str) -> str:
    """
    function for getting the something from the registry
    """
    try:

        return "something"
    except Exception as e:
        return f"Error getting something: {e}"