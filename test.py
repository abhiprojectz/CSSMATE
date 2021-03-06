from . import app
from sections import sections

def query_output(query):
	for query in ("please give me a button", "i want a button in github style",'i want a welcome page with a title and a subtitle','two columns flexbox', "give me a paragraph", "a circle", "two buttons seperated inside a box", "one button at left and another at right"):
	    uid = np.argmax(embeddings.similarity(query, sections))

	    # print("%-50s %s" % (query, sections[uid]))

	return sections[uid]



if '__name__' == "__main__":
	query_output(query)