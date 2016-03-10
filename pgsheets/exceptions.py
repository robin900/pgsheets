class PGSheetsException(Exception):
    pass


class PGSheetsHTTPException(PGSheetsException):
    pass


class PGSheetsValueError(PGSheetsException):
    pass


def _check_status(r):
    if r.status_code // 100 != 2:
        raise PGSheetsHTTPException(
            "Bad HTTP response {code}:\n{content}"
            .format(code=r.status_code, content=r.content.decode())
            )
