# FRED API Documentation

FRED is a tool that automatically produces RDF/OWL ontologies and linked data from natural language sentences. The underlying approach is based on Combinatory Categorial Grammar, Discourse Representation Theory, Linguistic Frames, and Ontology Design Patterns. The output is further enriched with Named Entity Recognition (NER) and Word Sense Disambiguation (WSD).

---

## Base URL and Endpoint

- **Host:** `wit.istc.cnr.it`
- **Scheme:** `http`
- **API Endpoint:** `/stlab-tools/fred`

---

## Authentication

This API uses Bearer token authentication. When making requests, include an `Authorization` header with your access token.

---

## Request Format

All API requests follow a general pattern similar to the example below:

```bash
curl -G \
  -H "Accept: application/rdf+xml" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  --data-urlencode text="Miles Davis was an american jazz musician" \
  http://wit.istc.cnr.it/stlab-tools/fred
```

**Notes:**

- The request method is **GET**.
- The output can be returned in multiple RDF formats. Use the `Accept` header to specify your preferred format (e.g., `application/rdf+xml`, `text/turtle`, etc.).

---

## Query Parameters

The API accepts several query parameters. Below is a detailed list:

### Required Parameter

- **`text`**
  - **Type:** string
  - **Description:** The input natural language text.
  - **Requirement:** Required

### Optional Parameters

- **`prefix`**
  - **Type:** string
  - **Description:** The prefix used for the namespace of terms introduced by FRED in the output. If not specified, `fred:` is used as the default.
  
- **`namespace`**
  - **Type:** string
  - **Description:** The namespace used for the terms introduced by FRED in the output. Defaults to `http://www.ontologydesignpatterns.org/ont/fred/domain.owl#` if not provided.

- **`wsd`**
  - **Type:** boolean
  - **Description:** Determines if Word Sense Disambiguation should be performed on input terms. Defaults to `false`.

- **`wfd`**
  - **Type:** boolean
  - **Description:** Enables Word Frame Disambiguation to align input terms with WordNet synsets, WordNet Super-senses, and Dolce classes. Defaults to `false`.

- **`wfd_profile`**
  - **Type:** string
  - **Description:** Specifies the profile associated with Word Frame Disambiguation.
  - **Allowed Values:** `b`, `d`, `t`
  - **Default:** `b`

- **`tense`**
  - **Type:** boolean
  - **Description:** If set to true, includes temporal relations between events based on their grammatical tense. Defaults to `false`.

- **`roles`**
  - **Type:** boolean
  - **Description:** If true, includes FrameNet roles in the resulting ontology. Defaults to `false`.

- **`textannotation`**
  - **Type:** string
  - **Description:** The vocabulary used for annotating text in RDF.
  - **Allowed Values:** `earmark`, `nif`
  - **Default:** `earmark`

- **`semantic-subgraph`**
  - **Type:** boolean
  - **Description:** If enabled, generates RDF that expresses only the core semantics of the sentence without additional triples (e.g., text spans, parts-of-speech). Defaults to `false`.

---

## Response Formats

The API can return RDF in various formats based on the `Accept` header:

- `application/rdf+xml`
- `text/turtle`
- `application/rdf+json`
- `text/rdf+n3`
- `text/rdf+nt`
- `image/png`

On a successful request (HTTP 200), the API returns the RDF data produced by FRED.

---

## Example Usage

Here’s an example of how to call the API using `curl`:

```bash
curl -G \
  -H "Accept: application/rdf+xml" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  --data-urlencode text="Miles Davis was an american jazz musician" \
  --data-urlencode tense=true \
  --data-urlencode wfd=true \
  http://wit.istc.cnr.it/stlab-tools/fred
```

**Explanation:**

- The `-G` flag sends the data as query parameters.
- Two headers are used:
  - `Accept: application/rdf+xml` requests the RDF/XML format.
  - `Authorization: Bearer <ACCESS_TOKEN>` passes your access token.
- The `--data-urlencode` option is used to properly encode the natural language text.
- Adjust other parameters (such as `wsd`, `wfd`, etc.) by appending additional `--data-urlencode` options as needed.