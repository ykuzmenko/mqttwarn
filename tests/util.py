# -*- coding: utf-8 -*-
# (c) 2018-2021 The mqttwarn developers
import time

from mqttwarn.configuration import load_configuration
from mqttwarn.core import bootstrap, load_services, on_message, start_workers
from paho.mqtt.client import MQTTMessage


def core_bootstrap(configfile=None):
    """
    Bootstrap the core machinery without MQTT
    """

    # Load configuration file
    config = load_configuration(configfile)

    # Bootstrap mqttwarn.core
    bootstrap(config=config, scriptname="testdrive")

    # Load services
    services = config.getlist("defaults", "launch")
    load_services(services)

    # Launch worker threads to operate on queue
    start_workers()


def send_message(topic=None, payload=None):

    # Mock an instance of an Eclipse Paho MQTTMessage
    message = MQTTMessage(mid=42, topic=topic.encode("utf-8"))
    if payload is not None:
        message.payload = payload.encode("utf-8")

    # Signal the message to the machinery
    on_message(None, None, message)

    # Give the machinery some time to process the message
    time.sleep(0.10)
