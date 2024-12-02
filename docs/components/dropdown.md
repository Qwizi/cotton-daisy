# Dropdown

| Argument   | Required | Type      | Default      | Description                                                                                                                          |
|------------|----------|-----------|--------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `title`    | Yes      | `string`  | `null`       | Specifies the button label or title for the dropdown trigger.                                                                        |
| `bg`       | No       | `string`  | `"base-100"` | Specifies the background color of the dropdown content. Options depend on your CSS (e.g., `primary`, `secondary`).                   |
| `rounded`  | No       | `boolean` | `true`       | Adds rounded corners to the dropdown content when set to `true`.                                                                     |
| `w`        | No       | `string`  | `"52"`       | Specifies the width of the dropdown content. Accepts numeric values or predefined CSS classes.                                       |
| `shadow`   | No       | `boolean` | `true`       | Applies a shadow to the dropdown content when set to `true`.                                                                         |
| `position` | No       | `string`  | `null`       | Specifies the position of the dropdown relative to the trigger. Options depend on your CSS (e.g., `top`, `bottom`, `left`, `right`). |
| `align`    | No       | `string`  | `null`       | Specifies the alignment of the dropdown content. Options depend on your CSS (e.g., `start`, `center`, `end`).                        |
| `hover`    | No       | `boolean` | `false`      | Enables the dropdown to open on hover instead of click.                                                                              |
| `open`     | No       | `boolean` | `false`      | Keeps the dropdown open when set to `true`.                                                                                          |

/// admonition | Component from DaisyUI
[https://daisyui.com/components/dropdown/](https://daisyui.com/components/dropdown/)
///

## Installation

```bash
cotton-daisy add dropdown
```

## Usage

/// Tab | Basic

```html

<c-dropdown title="Dropdown">
    <li>Edit</li>
    <li>Delete</li>
</c-dropdown>
```

///