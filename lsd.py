#!/usr/bin/env python3
import argparse

from controller import Controller
from repository import Repository
from logger import setup_uncaught_exceptions_logger, setup_default_loggers
from draw_controller import DrawController
from matrix import Matrix
from queue import Queue


def main():
    setup_uncaught_exceptions_logger()
    setup_default_loggers()

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', action='store', type=str, help='API base URL', required=True)
    parser.add_argument('-a', '--username', action='store', type=str, help='HTTP basic auth username')
    parser.add_argument('-p', '--password', action='store', type=str, help='HTTP basic auth password')
    args = parser.parse_args()

    # Create controller
    queue = Queue()
    repo = Repository(base_url=args.url, username=args.username, password=args.password)
    dc=DrawController(queue=queue, matrix=Matrix(width=32, hieght=16), refresh_rate=0.1)
    controller = Controller(repo=repo, queue=queue)

    controller.start_polling()


if __name__ == "__main__":
    main()
