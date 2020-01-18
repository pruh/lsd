import logging
import sys


log = logging.getLogger(__name__)


def setup_default_loggers() -> None:
    __setup_global_logging_levels()

    formatter = logging.Formatter(
        '%(asctime)s [%(threadName)18s][%(module)14s][%(levelname)8s] %(message)s')

    # Redirect messages lower or equal than INFO to stdout
    stdout_hdlr = logging.StreamHandler(sys.stdout)
    stdout_hdlr.setFormatter(formatter)
    log_filter = MaxLevelFilter(logging.INFO)
    stdout_hdlr.addFilter(log_filter)
    stdout_hdlr.setLevel(logging.DEBUG)

    # Redirect messages higher or equal than WARNING to stderr
    stderr_hdlr = logging.StreamHandler(sys.stderr)
    stderr_hdlr.setFormatter(formatter)
    stderr_hdlr.setLevel(logging.WARNING)

    log = logging.getLogger()
    log.addHandler(stdout_hdlr)
    log.addHandler(stderr_hdlr)


def __setup_global_logging_levels():
    root_log = logging.getLogger()
    root_log.setLevel(logging.DEBUG)

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def setup_uncaught_exceptions_logger():
    sys.excepthook = __handle_exception


def __handle_exception(exc_type, exc_value, exc_traceback):
    """
    Redirect uncaught exceptions to logger.
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    log.error(f"Uncaught exception: {exc_value}",
              exc_info=(exc_type, exc_value, exc_traceback))


class MaxLevelFilter(object):

    def __init__(self, max_level):
        self.__max_level = max_level

    def __eq__(self, other):
        return isinstance(other, MaxLevelFilter) and self.__max_level == other.__max_level

    def filter(self, record):
        return record.levelno <= self.__max_level
