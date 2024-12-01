# Alert

| Argument      | Required | Type      | Default   | Description                                                                               |
|---------------|----------|-----------|-----------|-------------------------------------------------------------------------------------------|
| `type`        | No       | `string`  | `null`    | Specifies the type of the alert. Options are: `info`, `success`, `warning`, `error`.      |
| `title`       | No       | `string`  | `null`    | The title of the alert. Appears in bold above the description text.                       |
| `description` | No       | `string`  | `null`    | A brief description or additional information about the alert.                            |
| `shadow`      | No       | `boolean` | `true`    | Adds a shadow effect to the alert box. Can be set to `false` to remove the shadow.        |
| `text`        | No       | `string`  | `"white"` | Sets the text color of the alert. Accepts any valid text color class, e.g., `text-black`. |

/// admonition | Component from DaisyUI
[https://daisyui.com/components/alert/](https://daisyui.com/components/alert/)
///

## Installation

```bash
cotton-daisy add alert
```

## Usage

```html
<c-alert type="info" title="Info Alert" description="Info alert description"/>
```
