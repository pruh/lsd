#!/usr/bin/env python3

from controller import Controller
from repo import Repo


def main():
    # Create controller
    controller = Controller(repo=Repo())

    controller.start_polling()


if __name__ == "__main__":
    main()