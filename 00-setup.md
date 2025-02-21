- [Cisco Devnet Sandbox](#cisco-devnet-sandbox)
- [Postman](#postman)
  - [Visualizer](#visualizer)

# Cisco Devnet Sandbox


# Postman

* [Postman workspace](https://web.postman.co/)
* examples
  * https://github.com/dbell-infra/enauto_examples
  * https://github.com/ebarredo84/sw_enauto_prep/blob/main/enauto_functions_sdwan_ebo.py

## Visualizer

* by chatGPT

```
// Parse the response
let jsonData = pm.response.json();

// Extract the columns array and data
let columns = jsonData.header.columns;
let rows = jsonData.data; // Assuming your data is under 'data', adjust accordingly

// Create table headers from columns
let headers = columns.map(column => column.title);

// Generate the table rows
let rowData = rows.map(row => 
    columns.map(column => `<td>${row[column.property] || ''}</td>`).join("")
);

// Create the HTML table structure
let table = `
    <table border="1" style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr>${headers.map(header => `<th>${header}</th>`).join("")}</tr>
        </thead>
        <tbody>
            ${rowData.map(row => `<tr>${row}</tr>`).join("")}
        </tbody>
    </table>
`;

// Set the visualizer to display the table
pm.visualizer.set(table);
```