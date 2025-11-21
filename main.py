"""Main runner - small wrapper to run the Streamlit web UI from `webui.py`."""

from webui import main as run_app


if __name__ == "__main__":
    # Prefer to run via `streamlit run main.py`, but allow `python main.py` for quick tests.
    run_app()