import argparse
from app.rag import ask_rag
from app.ingest import run_ingestion


def main():
    parser = argparse.ArgumentParser(description="Local RAG System")

    parser.add_argument(
        "--ingest",
        action="store_true",
        help="Run document ingestion"
    )

    parser.add_argument(
        "--question",
        type=str,
        help="Ask a question"
    )

    args = parser.parse_args()

    if args.ingest:
        run_ingestion()
        return

    if args.question:
        answer = ask_rag(args.question)
        print("\nAnswer:\n")
        print(answer)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
