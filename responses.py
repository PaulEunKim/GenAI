def handle_response(message) -> str:

    if (p_message := message.lower()) == 'hello':
        return 'Hey there!'
