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

/// Tab | Basic

```html

<c-alert title="Info Alert" description="Info alert description"/>
```

///

/// Tab | Info

```html

<c-alert type="info" title="Info Alert" description="Info alert description"/>
```

///

/// Tab | Success

```html

<c-alert type="success" title="Success Alert" description="Success alert description"/>
```

///

/// Tab | Warning

```html

<c-alert type="warning" title="Warning Alert" description="Warning alert description"/>
```

///

/// Tab | Error

```html

<c-alert type="error" title="Error Alert" description="Error alert description"/>
```

///

/// Tab | Custom content

```html

<c-alert type="info">
    <h2>Custom content</h2>
</c-alert>
```

```html

<c-alert type="info">
    <c-slot name="title">
        <h2>Custom title</h2>
    </c-slot>
    <c-slot name="description">
        <p>Custom description</p>
</c-alert>
```
///