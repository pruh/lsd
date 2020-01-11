#!/usr/bin/env python3

from controller import Controller

def main():
    # Create controller
    controller = Controller()

    controller.start_polling()


if __name__ == "__main__":
    main()