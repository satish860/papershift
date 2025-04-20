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