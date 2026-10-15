from pprint import pprint

from app.main import collect_metrics


def main():
    print()
    print("=" * 50)
    print("SERVERWATCH v0.1")
    print("=" * 50)

    metrics = collect_metrics()

    pprint(metrics)

    print("=" * 50)


if __name__ == "__main__":
    main()