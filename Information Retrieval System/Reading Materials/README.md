# Information Retrieval System


- ## Types of queries
	- 1. Keyword Queries :
		- Simplest and most common queries.
		- The user enters just keyword combinations to retrieve documents.
		- These keywords are connected by logical AND operator.
		- All retrieval models provide support for keyword queries.
	- 2. Boolean Queries :
		- Some IR systems allow using +, -, AND, OR, NOT, ( ), Boolean operators in combination of keyword formulations.
		- No ranking is involved because a document either satisfies such a query or does not satisfy it.
		- A document is retrieved for boolean query if it is logically true as exact match in document.
	- 3. Phase Queries :
		- When documents are represented using an inverted keyword index for searching, the relative order of items in document is lost.
		- To perform exact phase retrieval, these phases are encoded in inverted index or implemented differently.
		- This query consists of a sequence of words that make up a phase.
		- It is generally enclosed within double quotes.
	- 4. Proximity Queries :
		- Proximity refers ti search that accounts for how close within a record multiple items should be to each other.
		- Most commonly used proximity search option is a phase search that requires terms to be in exact order.
		- Other proximity operators can specify how close terms should be to each other. Some will specify the order of search terms.
		- Search engines use various operators names such as NEAR, ADJ (adjacent), or AFTER.
		- However, providing support for complex proximity operators becomes expensive as it requires time-consuming pre-processing of documents and so it is suitable for smaller document collections rather than for web.
	- 5. Wildcard Queries :
		- It supports regular expressions and pattern matching-based searching in text.
		- Retrieval models do not directly support for this query type.
		- In IR systems, certain kinds of wildcard search support may be implemented. Example: usually words ending with trailing characters.
	- 6. Natural Language Queries :
		- There are only a few natural language search engines that aim to understand the structure and meaning of queries written in natural language text, generally as question or narrative.
		- The system tries to formulate answers for these queries from retrieved results.
		- Semantic models can provide support for this query type.

- ## Semantic Search engine
	- Semantic search is the process search engines use to try to understand the intent and contextual meaning of your search query in order to give you results that match what you had in mind.
	- Google's semantic search attempts to improve on the search formula intended to produce relevant search results for web users by creating rules that define a searcher's intent and the contextual meaning of search terms.

- ## Relevance Feedback
	- The idea of relevance feedback ( ) is to involve the user in the retrieval process so as to improve the final result set. In particular, the user gives feedback on the relevance of documents in an initial set of results. The basic procedure is:

		- The user issues a (short, simple) query.
		- The system returns an initial set of retrieval results.
		- The user marks some returned documents as relevant or nonrelevant.
		- The system computes a better representation of the information need based on the user feedback.
		- The system displays a revised set of retrieval results.
	- Relevance feedback can go through one or more iterations of this sort. The process exploits the idea that it may be difficult to formulate a good query when you don't know the collection well, but it is easy to judge particular documents, and so it makes sense to engage in iterative query refinement of this sort. In such a scenario, relevance feedback can also be effective in tracking a user's evolving information need: seeing some documents may lead users to refine their understanding of the information they are seeking.

	- query *(revised query)* ---> `Search Engine` ---> responses *(examine and label responses)*
	- Methods : 
	- **1. Rocchio algorithm**
		- The Rocchio Algorithm is the classic algorithm for implementing relevance feedback. It models a way of incorporating relevance feedback information into the vector space model
		- addition or removal of keywords
		- revised query
			- suppose if we have 5 keywords k1,k2,k3,k4,k5 in which we find that k3 term is present in most of the non relavant documents then we will revise our query by removing the term k3.
			- also if we find certain keywords which are not present in the query but are found in most of every relavant document then we should revise our query by adding that term
	- **2. Semi-supervised learning *(LU learning)* **
		- L-U Learning
			- Since the number of user-selected relevant and irrelevant documents may be small, it can be difficult to build an accurate classifier. However, unlabeled examples, i.e., those documents that are not selected by the user, can be utilized to improve learning to produce a more accurate classifier. This fits the LU learning model exactly (see Sect. 5.1). The user-selected relevant and irrelevant documents form the small labeled training set.
		- P-U Learning (positive unlabeled)
			- if user does not label the webpage then we will train the model with labelled webpage and will label labelled webpage
			
			> The two learning models mentioned above assume that the user can confidently identify both relevant and irrelevant documents. However, in some cases, the user only selects (or clicks) documents that he/she feels relevant based on the title or summary information (e.g., snippets in Web search), which are most likely to be true relevant documents, but does not indicate irrele- vant documents. Those documents that are not selected by the user may not be treated as irrelevant because he/she has not seen them. Thus, they can only be regarded as unlabeled documents. This is called implicit feed- back. In order to learn in this case, we can use PU learning, i.e., learning from positive and unlabeled examples (see Sect. 5.2). We regard the user- selected documents as positive examples, and unselected documents as unlabeled examples. Researchers have experimented with this approach in the Web search context and obtained good results

	- Relevance feedback on the web
		- Some web search engines offer a similar/related pages feature: the user indicates a document in the results set as exemplary from the standpoint of meeting his information need and requests more documents like it. This can be viewed as a particular simple form of relevance feedback. However, in general relevance feedback has been little used in web search. One exception was the Excite web search engine, which initially provided full relevance feedback. However, the feature was in time dropped, due to lack of use. On the web, few people use advanced search interfaces and most would like to complete their search in a single interaction. But the lack of uptake also probably reflects two other factors: relevance feedback is hard to explain to the average user, and relevance feedback is mainly a recall enhancing strategy, and web search users are only rarely concerned with getting sufficient recall.

	- **3. Indirect relevance feedback**
		- We can also use indirect sources of evidence rather than explicit feedback on relevance as the basis for relevance feedback. This is often called implicit (relevance) feedback . Implicit feedback is less reliable than explicit feedback, but is more useful than pseudo relevance feedback, which contains no evidence of user judgments. Moreover, while users are often reluctant to provide explicit feedback, it is easy to collect implicit feedback in large quantities for a high volume system, such as a web search engine.
		- On the web, DirectHit introduced the idea of ranking more highly documents that users chose to look at more often. In other words, clicks on links were assumed to indicate that the page was likely relevant to the query. This approach makes various assumptions, such as that the document summaries displayed in results lists (on whose basis users choose which documents to click on) are indicative of the relevance of these documents. In the original DirectHit search engine, the data about the click rates on pages was gathered globally, rather than being user or query specific. This is one form of the general area of clickstream mining . Today, a closely related approach is used in ranking the advertisements that match a web search query 

	- **4. Pseudo Relevance Feedback **
		- Pseudo relevance feedback , also known as blind relevance feedback , provides a method for automatic local analysis. It automates the manual part of relevance feedback, so that the user gets improved retrieval performance without an extended interaction. The method is to do normal retrieval to find an initial set of most relevant documents, to then assume that the top $k$ ranked documents are relevant, and finally to do relevance feedback as before under this assumption.
	
- ## Latent Semantic Indexing

	- The retrieval models discussed so far are based on keyword or term matching, i.e., matching terms in the user query with those in the documents. However, many concepts or objects can be described in multiple ways (using different words) due to the context and people’s language habits. If a user query uses different words from the words used in a document, the document will not be retrieved although it may be relevant because the document uses some symonyms of the words in the user query. This causes low recall. For example, “picture”, “image” and “photo” are synonyms in the context of digital cameras. If the user query only has the word “picture”, relevant documents that contain “image” or “photo” but not “picture” will not be retrieved.
	- Latent semantic indexing (LSI), proposed by Deerwester et al. [125], aims to deal with this problem through the identification of statistical associations of terms. It is assumed that there is some underlying latent semantic structure in the data that is partially obscured by the randomness of word choice. It then uses a statistical technique, called singular value decomposition (SVD) [203], to estimate this latent structure, and to remove the “noise”. The results of this decomposition are descriptions of terms and documents based on the latent semantic structure derived from SVD. This structure is also called the hidden “concept” space, which associates syntactically different but semantically similar terms and documents. These transformed terms and documents in the “concept” space are then used in retrieval, not the original terms or documents. Furthermore, the query is also transformed into the “concept” space before retrieval.
	- Let D be the text collection, the number of distinctive words in D be m and the number of documents in D be n. LSI starts with an m�n term-document matrix A. Each row of A represents a term and each column represents a document. The matrix may be computed in various ways, e.g., using term frequency or TF-IDF values. We use term frequency as an example in this section. Thus, each entry or cell of the matrix A, denoted by Aij, is the number of times that term i occurs in document j.

- ## Markov Model
	- A Markov Model is a *stochastic* model which models temporal or sequential data, i.e., data that are ordered.
	- It provides a way to model the dependencies of current information (e.g. weather) with previous information.
	-  It is composed of states, transition scheme between states, and emission of outputs (discrete or continuous).
	-  Several goals can be accomplished by using Markov models:
		- Learn **statistics** of sequential data.
		- Do **prediction** or estimation.
		- Recognize **patterns**.

- Hidden Markov Model (HMM)?
	- A Hidden Markov Model, is a stochastic model where the states of the model are hidden. Each state can emit an output which is observed.
	- Imagine: You were locked in a room for several days and you were asked about the weather outside. The only piece of evidence you have is whether the person who comes into the room bringing your daily meal is carrying an umbrella or not.
 	- What is hidden? Sunny, Rainy, Cloudy
	- What can you observe? Umbrella or Not
	- HMM Parameters:
		- Transition probabilities 𝑃(𝑞𝑖|𝑞𝑖−1)
		- Emission probabilities 𝑃(𝑜𝑖|𝑞𝑖)
		- Initial state probabilities 𝑃(𝑞𝑖)
		
		- A HMM is governed by the following parameters:
			- λ = {𝐴,𝐵,𝜋}
				- State-transition probability matrix 𝐴
				- Emission/Observation/State Conditional Output probabilities 𝐵
				- Initial (prior) state probabilities 𝜋
			- Determine the fixed number of states (𝑁):
				- 𝑆 = 𝑠1,...,𝑠𝑁
		
		
	- Emission probabilities: A state will generate an observation (output), but a decision must be taken according on how to model the output, i.e., as discrete or continuous.
		- Discrete outputs are modeled using pmfs.	*(Probability Mass Function)*
		- Continuous outputs are modeled using pdfs.	*(Probability Density Function)*
	
	- NEXT steps : 
		- **State Sequence Decoding** (Viterbi Algorithm): Given a HMM we can find the best single state sequence (path) Q = q<sub>1</sub>, ... , q<sub>T</sub> that best explains a known observation sequence 𝑂 = o<sub>1</sub>, ... , o<sub>T</sub>.
			> given HMM, find state sequence
		- **Observation Sequence Evaluation** (Forward- Backward Algorithm): Evaluate a sequence of observations 𝑂 = o<sub>1</sub>, ... , o<sub>𝑇</sub> given several alternative HMMs, and determine which one best recognizes the observation sequence (classification).
			> given HMM, find observation sequence
