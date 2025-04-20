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