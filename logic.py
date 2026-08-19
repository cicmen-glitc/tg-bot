from transformers import pipeline


_classifier = None


def _get_classifier():
	global _classifier

	if _classifier is None:
		_classifier = pipeline(
			"sentiment-analysis",
			model="nlptown/bert-base-multilingual-uncased-sentiment",
		)

	return _classifier


def analyze_text(text):
	result = _get_classifier()(text)[0]
	stars = int(result["label"].split()[0])
	if stars <= 2:
		label = "NEGATIVE"
	elif stars == 3:
		label = "NEUTRAL"
	else:
		label = "POSITIVE"
	return label, result["score"]
