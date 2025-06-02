"""
This module provides functionality for publishing messages to RabbitMQ queues.
It uses aio_pika for asynchronous message queue operations.
"""

import aio_pika
from iam.core.config import settings


async def publish_event(queue: str, message: str):
    """Publishes a message to a RabbitMQ queue.

    Args:
        queue (str): The name of the queue to publish to.
        message (str): The message content to be published.

    Returns:
        None
    """
    connection = await aio_pika.connect_robust(
        settings.RABBITMQ_URL,
    )
    channel = await connection.channel()
    await channel.declare_queue(queue, durable=True)
    await channel.default_exchange.publish(
        aio_pika.Message(
            body=message.encode(),
        ),
        routing_key=queue,
    )
