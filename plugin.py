import json, urllib, os

def results(parsed, original_query):
	q = parsed['wikipedia_query'] if 'wikipedia_query' in parsed else parsed['~wikipedia_query']
	url = "https://en.m.wikipedia.org/wiki/Special:search/{0}".format(urllib.quote(q.replace(' ', '_')))
	html = """
	<script>
	setTimeout(function() {
		window.location = %s;
	}, 500); // throttle a little
	</script>
	""" % (json.dumps(url))
	return {
		"title": "Search Wikipedia '{0}'".format(q),
		"html": html,
		"run_args": [q]
	}

def run(query):
	url = "https://en.wikipedia.org/wiki/Special:search/{0}".format(urllib.quote_plus(query))
	os.system("open {0}".format(json.dumps(url)))
