#!/usr/bin/env python
import logging
from controller.local_controller import LocalController
import argparse

parser = argparse.ArgumentParser(description="Adaptive Parallel Execution Engine")
parser.add_argument('--config', action = "store", help = "Controller config file",
                    type = str, required = False)
parser.add_argument('--broker-config', action = "store", help = "Broker config file",
                    default="configs/broker-config.json", type = str, required = False)
parser.add_argument('--optimizer-config', action = "store", help = "Optimizer config file",
                    type = str, required = False)
parser.add_argument('--commands-file', action = "store", help = "Controller commands file",
                    type = str, required = False)

def main():
    print("Starting execution engine!")
    logging.basicConfig(filename='cosmos.log', level=logging.INFO)

    args = parser.parse_args()
    cconfig = args.config
    bconfig = args.broker_config
    oconfig = args.optimizer_config
    commands_file = args.commands_file

    controller = LocalController()
    controller.parse_config(controller_config=cconfig,
                            optimizer_config=oconfig,
                            broker_config=bconfig)

    controller.parse_commands_file(commands_file)

    controller.main_loop()

    print("Execution engine finished! Exiting now.")

if __name__ == '__main__':
    main()



