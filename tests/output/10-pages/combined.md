## Page 1

OmniAl API Docs
# Welcome to the OmniAI Document API! :rocket:

How does it work?
To run document OCR with OmniAl, pass a **file** or **url** the **/extract** endpoint.
- Optionally pass in a desired JSON schema to extract structured output from that document. To run OCR without extracted response, simply omit the **schema** argument.
- This is an asynchronous api endpoint. The initial request will return a jobld.

**Extract: POST /extract**

Request Headers:
An API Key is required to access this endpoint.

<table>
  <tr>
    <th>Name</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>x-api-key</td>
    <td>your_api_key</td>
  </tr>
</table>

Params
Either input File or URL is required but not more than one. See accepted file types below.

<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
   <tr>
    <td>url</td>
    <td>string</td>
    <td>URL of the document used for extraction</td>
  </tr>
   <tr>
    <td>file</td>
    <td>file</td>
    <td>File used for extraction</td>
  </tr>
   <tr>
    <td>schema</td>
    <td>JSON (optional)</td>
    <td>JSON schema</td>
  </tr>
   <tr>
    <td>maintainFormat</td>
    <td>boolean</td>
    <td>Maintains format from the previous page. Defaults to false</td>
  </tr>
</table>

```
curl -X POST https://api.getomni.ai/extract \
-H "x-api-key: my-api-key" \
-F "file=@path/to/your/file.pdf"
```

<page_number>1</page_number>


---

## Page 2

OmniAl API Docs

# Welcome to the OmniAI Document API! 🚀

How does it work?
To run document OCR with OmniAl, pass a **file** or **url** the **/extract** endpoint.
- Optionally pass in a desired JSON schema to extract structured output from that document. To run OCR without extracted response, simply omit the **schema** argument.
- This is an asynchronous api endpoint. The initial request will return a jobld.

Extract: **POST** /extract

Request Headers:
An API Key is required to access this endpoint.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>x-api-key</td>
      <td>your_api_key</td>
    </tr>
  </tbody>
</table>

Params
Either input File or URL is required but not more than one. See accepted file types below.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>url</td>
      <td>string</td>
      <td>URL of the document used for extraction</td>
    </tr>
    <tr>
      <td>file</td>
      <td>file</td>
      <td>File used for extraction</td>
    </tr>
    <tr>
      <td>schema</td>
      <td>JSON (optional)</td>
      <td>JSON schema</td>
    </tr>
    <tr>
      <td>maintainFormat</td>
      <td>boolean</td>
      <td>Maintains format from the previous page. Defaults to false</td>
    </tr>
  </tbody>
</table>

```
curl -X POST https://api.getomni.ai/extract \
-H "x-api-key: my-api-key" \
-F "file=@path/to/your/file.pdf"
```

<page_number>1</page_number>

---

## Page 3

OmniAI API Docs

# Welcome to the OmniAI Document API! 🚀

#### How does it work?
To run document OCR with OmniAI, pass a **file** or **url** the **/extract** endpoint.
  - Optionally pass in a desired JSON schema to extract structured output from that document. To run OCR without extracted response, simply omit the **schema** argument.
  - This is an asynchronous api endpoint. The initial request will return a jobld.

## Extract: `POST /extract`

#### Request Headers:
An API Key is required to access this endpoint.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>x-api-key</td>
      <td>`your_api_key`</td>
    </tr>
  </tbody>
</table>

#### Params
Either input File or URL is required but not more than one. See accepted file types below.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>url</td>
      <td>string</td>
      <td>URL of the document used for extraction</td>
    </tr>
    <tr>
      <td>file</td>
      <td>file</td>
      <td>File used for extraction</td>
    </tr>
    <tr>
      <td>schema</td>
      <td>JSON (optional)</td>
      <td>JSON schema</td>
    </tr>
    <tr>
      <td>maintainFormat</td>
      <td>boolean</td>
      <td>Maintains format from the previous page. Defaults to `false`</td>
    </tr>
  </tbody>
</table>

```bash
curl -X POST https://api.getomni.ai/extract \
-H "x-api-key: my-api-key" \
-F "file=@path/to/your/file.pdf"
```

<page_number>1</page_number>

---

## Page 4

OmniAl
API Docs
# Welcome to the OmniAI Document API! :rocket:

## How does it work?
To run document OCR with OmniAl, pass a **file** or **url** the **/extract** endpoint.
  - Optionally pass in a desired JSON **schema** to extract structured output from that document. To run OCR without extracted response, simply omit the **schema** argument.
  - This is an asynchronous api endpoint. The initial request will return a jobld.

## Extract: **POST** /extract
### Request Headers:
An API Key is required to access this endpoint.

<table>
  <tr>
    <th>Name</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>x-api-key</td>
    <td>your_api_key</td>
  </tr>
</table>

### Params
Either input File or URL is required but not more than one. See accepted file types below.

<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>url</td>
    <td>string</td>
    <td>URL of the document used for extraction</td>
  </tr>
  <tr>
    <td>file</td>
    <td>file</td>
    <td>File used for extraction</td>
  </tr>
   <tr>
    <td>schema</td>
    <td>JSON (optional)</td>
    <td>JSON schema</td>
  </tr>
  <tr>
    <td>maintainFormat</td>
    <td>boolean</td>
    <td>Maintains format from the previous page. Defaults to false</td>
  </tr>
</table>

```
curl -X POST https://api.getomni.ai/extract \
-H "x-api-key: my-api-key" \
-F "file=@path/to/your/file.pdf"
```
<page_number>1</page_number>

---

## Page 5

OmniAI
API Docs
# Welcome to the OmniAI Document API! 🚀

How does it work?
To run document OCR with OmniAI, pass a **file** or **url** the **/extract** endpoint.
- Optionally pass in a desired JSON **schema** to extract structured output from that document. To run OCR without extracted response, simply omit the **schema** argument.
- This is an asynchronous api endpoint. The initial request will return a jobld.

## Extract: `POST /extract`

### Request Headers:
An API Key is required to access this endpoint.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>x-api-key</td>
      <td>`your_api_key`</td>
    </tr>
  </tbody>
</table>

### Params
Either input File or URL is required but not more than one. See accepted file types below.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>url</td>
      <td>string</td>
      <td>URL of the document used for extraction</td>
    </tr>
    <tr>
      <td>file</td>
      <td>file</td>
      <td>File used for extraction</td>
    </tr>
   <tr>
      <td>schema</td>
      <td>JSON (optional)</td>
      <td>JSON schema</td>
    </tr>
    <tr>
      <td>maintainFormat</td>
      <td>boolean</td>
      <td>Maintains format from the previous page. Defaults to false</td>
    </tr>
  </tbody>
</table>

```
curl -X POST https://api.getomni.ai/extract \
-H "x-api-key: my-api-key" \
-F "file=@path/to/your/file.pdf"
```

<page_number>1</page_number>

---

## Page 6

OmniAl API Docs

# Welcome to the OmniAI Document API! 🚀

## How does it work?

To run document OCR with OmniAl, pass a `file` or `url` the `/extract` endpoint.
- Optionally pass in a desired JSON `schema` to extract structured output from that document. To run OCR without extracted response, simply omit the `schema` argument.
- This is an asynchronous api endpoint. The initial request will return a jobld.

## Extract: `POST` `/extract`

### Request Headers:
An API Key is required to access this endpoint.

<table>
  <tr>
    <th>Name</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>x-api-key</td>
    <td>`your_api_key`</td>
  </tr>
</table>

### Params
Either input File or URL is required but not more than one. See accepted file types below.

<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>url</td>
    <td>string</td>
    <td>URL of the document used for extraction</td>
  </tr>
  <tr>
    <td>file</td>
    <td>file</td>
    <td>File used for extraction</td>
  </tr>
    <tr>
    <td>schema</td>
    <td>JSON (optional)</td>
    <td>JSON schema</td>
  </tr>
    <tr>
    <td>maintainFormat</td>
    <td>boolean</td>
    <td>Maintains format from the previous page. Defaults to `false`</td>
  </tr>
</table>

```
curl -X POST https://api.getomni.ai/extract \
-H "x-api-key: my-api-key" \
-F "file=@path/to/your/file.pdf"
```
<page_number>1</page_number>

---

## Page 7

OmniAI
API Docs
# Welcome to the OmniAI Document API! 🚀
How does it work?
To run document OCR with OmniAl, pass a **file** or **url** the **/extract** endpoint.
- Optionally pass in a desired JSON schema to extract structured output from that document. To run OCR without extracted response, simply omit the **schema** argument.
- This is an asynchronous api endpoint. The initial request will return a jobld.
# Extract: **POST** /extract
Request Headers:
An API Key is required to access this endpoint.
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>x-api-key</td>
            <td>your_api_key</td>
        </tr>
    </tbody>
</table>

Params
Either input File or URL is required but not more than one. See accepted file types below.
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>url</td>
            <td>string</td>
            <td>URL of the document used for extraction</td>
        </tr>
        <tr>
            <td>file</td>
            <td>file</td>
            <td>File used for extraction</td>
        </tr>
        <tr>
            <td>schema</td>
            <td>JSON (optional)</td>
            <td>JSON schema</td>
        </tr>
        <tr>
            <td>maintainFormat</td>
            <td>boolean</td>
            <td>Maintains format from the previous page. Defaults to false</td>
        </tr>
    </tbody>
</table>

```
curl -X POST https://api.getomni.ai/extract \
-H "x-api-key: my-api-key" \
-F "file=@path/to/your/file.pdf"
```
<page_number>1</page_number>

---

## Page 8

OmniAl API Docs

# Welcome to the OmniAI Document API! 🚀

How does it work?

To run document OCR with OmniAl, pass a **file** or **url** the **/extract** endpoint.
*   Optionally pass in a desired JSON schema to extract structured output from that document. To run OCR without extracted response, simply omit the **schema** argument.
*   This is an asynchronous api endpoint. The initial request will return a jobld.

Extract: **POST** /extract

Request Headers:
An API Key is required to access this endpoint.

<table>
    <tr>
        <th>Name</th>
        <th>Value</th>
    </tr>
    <tr>
        <td>x-api-key</td>
        <td>your_api_key</td>
    </tr>
</table>

Params
Either input File or URL is required but not more than one. See accepted file types below.

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>url</td>
        <td>string</td>
        <td>URL of the document used for extraction</td>
    </tr>
    <tr>
        <td>file</td>
        <td>file</td>
        <td>File used for extraction</td>
    </tr>
    <tr>
        <td>schema</td>
        <td>JSON (optional)</td>
        <td>JSON schema</td>
    </tr>
    <tr>
        <td>maintainFormat</td>
        <td>boolean</td>
        <td>Maintains format from the previous page. Defaults to false</td>
    </tr>
</table>

```
curl -X POST https://api.getomni.ai/extract \
-H "x-api-key: my-api-key" \
-F "file=@path/to/your/file.pdf"
```

<page_number>1</page_number>

---

## Page 9

OmniAl
API Docs

# Turn any document into structured data

OCR is great! But the real magic comes from turning documents into beautiful structured JSON.
Plug in a schema to the extract endpoint to return JSON output alongside your

## Why do people love OmniAl?

<table>
<tr>
    <td>OCR that *just works*</td>
    <td>54.5%</td>
</tr>
<tr>
    <td>Understand charts and tables</td>
    <td>27.3%</td>
</tr>
<tr>
    <td>No issues with handwriting</td>
    <td>9.1%</td>
</tr>
<tr>
    <td>Structured data extraction</td>
    <td>9.1%</td>
</tr>
</table>

## Using a Schema

The `/extract` endpoint takes in an optional **schema** argument (example format below).

When passed in, the OCR result will be mapped to the specific JSON format you configured.

This is type safe. All responses will be validated against the input schema.

```json
1 {
2   "type": "object",
3   "properties": {
4     "omniai_benefits": {
5       "type": "array",
6       "description": "Reasons to use OmniAI",
7       "items": {
8         "type": "object",
9         "properties": {
10          "benefit": {
11            "type": "string",
12            "description": "Section label from the chart"
13          },
14          "percentage": {
15            "type": "number",
16            "description": "Percentage on a scale of -1. 00 to 1.00"
17          }
18        }
19      }
20    }
21  }
22 }
```
<page_number>2</page_number>

---

## Page 10

OmniAl
API Docs

We can accept any of the following document types:
PDF's, Docx, PPT, and images are the most common document types, but we support just about everything. As long as we can convert the file to a visual format, it should work!

```
[
    "pdf", // Portable Document Format
    "doc", // Microsoft Word 97-2003
    "docx", // Microsoft Word 2007-2019
    "odt", // OpenDocument Text
    "ott", // OpenDocument Text Template
    "rtf", // Rich Text Format
    "txt", // Plain Text
    "html", // HTML Document
    "htm", // HTML Document (alternative extension)
    "xml", // XML Document
    "wps", // Microsoft Works Word Processor
    "wpd", // WordPerfect Document
    "xls", // Microsoft Excel 97-2003
    "xlsx", // Microsoft Excel 2007-2019
    "ods", // OpenDocument Spreadsheet
    "ots", // OpenDocument Spreadsheet Template
    "csv", // Comma-Separated Values
    "tsv", // Tab-Separated Values
    "ppt", // Microsoft PowerPoint 97-2003
    "pptx", // Microsoft PowerPoint 2007-2019
    "odp", // OpenDocument Presentation
    "otp", // OpenDocument Presentation Template
];
```

Flexible Pricing
Get started with our document extraction api. For more complex workflows, try out our platform for more complex workflows, or batch document processing.

<br>

<table>
   <tr>
      <th>API</th>
      <th>Platform</th>
      <th>Enterprise</th>
   </tr>
   <tr>
      <td>$500/month</td>
      <td>$2,000/month</td>
      <td>Priced to fit your needs</td>
   </tr>
   <tr>
      <td>Get access to:</td>
      <td>Everything in API, plus:</td>
      <td>Everything in Platform, plus:</td>
   </tr>
   <tr>
      <td>Includes 10,000 pages per month</td>
      <td>Includes 50,000 pages per month</td>
      <td>Unlimited Documents</td>
   </tr>
    <tr>
      <td>$0.01 per page afterwards</td>
      <td>Custom Document Pipelines</td>
      <td>Connect to custom Models</td>
   </tr>
   <tr>
      <td>Structured data extraction</td>
      <td>Batch requests</td>
      <td>Fine Tuning</td>
   </tr>
   <tr>
      <td>Up to 100 pages per document</td>
      <td>Table automations</td>
      <td>SSO / SAML</td>
   </tr>
   <tr>
      <td>Up to 2 seats</td>
      <td>Data Connectors</td>
      <td>Export to Snowflake</td>
   </tr>
   <tr>
      <td></td>
      <td>Export to Sheets</td>
      <td>VPC Deployment</td>
   </tr>
   <tr>
      <td></td>
      <td>No page limit on documents</td>
      <td>Unlimited seats</td>
   </tr>
   <tr>
      <td></td>
      <td>Up to 10 seats</td>
      <td></td>
   </tr>
</table>

<page_number>3</page_number>