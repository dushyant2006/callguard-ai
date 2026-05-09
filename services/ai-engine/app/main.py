from app.events.consumer import CallEventConsumer

def main():
    print("Starting AI Engine Worker...")
    consumer = CallEventConsumer()
    consumer.start()

if __name__ == "__main__":
    main()
