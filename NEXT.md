# Session 3: data + baseline model

1. **Get the data.** I suggest the Bitext customer-support dataset on Hugging Face: 27 intents assigned to 10 categories, 26872 question/answer pairs, around 1000 per intent. It's licensed cdla-sharing-1.0, and its columns include instruction (the ticket text) plus the category and intent labels. Download the CSV into `data/` and add `data/` to `.gitignore`.
2. **Add `data.py`:** load the CSV and make a stratified train/test split with a fixed seed. Write a test that checks the split sizes and that each class appears in both sets.
3. **Add `model.py`:** a scikit-learn `Pipeline` with `TfidfVectorizer` → `LogisticRegression`, using `clean_text` as the preprocessor.

**Done when:** a script trains the model and prints accuracy on the test split.

**Honest caveat about this dataset:** the text is template-generated, so TF-IDF will probably score very high on `intent`. That's fine for v0, but it leaves little room to show the LLM cascade beating it in S3. If you want a harder number, use `intent` (27 classes) rather than `category`. Treat the score as a pipeline check, not as proof the model is good.

## Sessions after that

| Session | Work | S1 topic it covers |
|---|---|---|
| 4 | Write `macro_f1()` yourself and test it against `sklearn.metrics.f1_score`. Report macro-F1 on the test split. | B2 Metrics written yourself |
| 5 | mypy strict in CI. Typed signatures everywhere. | A11 Typing |
| 6 | CLI (`ticket-tagger train` / `predict "text"`), `logging` instead of `print`, config from env vars, save the model with joblib. | A11 Logging, config, CLI |
| 7 | `uv build` works, `AGENTS.md`, README with the CI badge, macro-F1 and the resume bullet. Close S1. | A11 Packaging, B15 |
