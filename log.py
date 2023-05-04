from typing import Optional
from inspect import currentframe


def log(error: Optional[str] = None,
        message: Optional[str] = None,
        driver: Optional[str] = None,
        end: Optional[str] = "") -> None:
    """
    Logs an error, printing it with additional information if provided.
    Parameters:
        error (str): The error message to log.
        message (str, optional): The message with user can use to send messages in console when the sys crash (default is None).
        driver (str, optional): The driver associated with the error (default is None).
    Returns:
        None
    """
    if error is None:
        if message is None:
            print("No error or message provided")

        else:
            print(f"{message}", end=f"{end}")

    else:
        error = f">> Error: {error}" if error is not None else "Error: Not informed"
        message = f">> Message: {message}" if message is not None else "Message: Not informed"
        filename = f">> File: {currentframe().f_back.f_code.co_filename}"
        line = f">> Line: {currentframe().f_back.f_lineno}"
        print("Erro")
        print("\n".join(filter(None, [filename, message, line, error])))

        if driver is not None:
            driver.quit()
