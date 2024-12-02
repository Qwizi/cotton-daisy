# Loading

| Argument | Required | Type     | Default     | Description                                                                                              |
|----------|----------|----------|-------------|----------------------------------------------------------------------------------------------------------|
| `type`   | No       | `string` | `"spinner"` | Specifies the type of the loading indicator. Options depend on your CSS (e.g., `spinner`, `dots`).       |
| `size`   | No       | `string` | `"md"`      | Defines the size of the loading indicator. Options depend on your CSS (e.g., `sm`, `md`, `lg`).          |
| `color`  | No       | `string` | `"primary"` | Sets the text color of the loading indicator. Options depend on your CSS (e.g., `primary`, `secondary`). |

/// admonition | Component from DaisyUI
[https://daisyui.com/components/loading/](https://daisyui.com/components/loading/)
///

## Installation

```bash
cotton-daisy add loading
```

## Usage

/// Tab | Basic

```html

<c-loading/>
```

///

/// Tab | Type

```html

<c-loading type="spinner"/>
<c-loading type="dots"/>
<c-loading type="ball"/>
<c-loading type="infinity"/>
<c-loading type="ring"/>
```

///

/// Tab | Size

```html

<c-loading size="sm"/>
<c-loading size="md"/>
<c-loading size="lg"/>
<c-loading size="xl"/>
```

///

/// Tab | Color

```html

<c-loading color="primary"/>
<c-loading color="secondary"/>
<c-loading color="success"/>
<c-loading color="warning"/>
<c-loading color="error"/>
```

///