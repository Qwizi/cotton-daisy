# Badge

| Argument           | Required | Type      | Default | Description                                                                                                   |
|--------------------|----------|-----------|---------|---------------------------------------------------------------------------------------------------------------|
| `type`             | No       | `string`  | `null`  | Specifies the type of the badge. Options can be custom and depend on your CSS (e.g., `primary`, `secondary`). |
| `outline`          | No       | `boolean` | `false` | Adds an outline style to the badge if set to `true`.                                                          |
| `size`             | No       | `string`  | `null`  | Specifies the size of the badge. Options can be custom and depend on your CSS (e.g., `lg`, `sm`).             |

/// admonition | Component from DaisyUI
[https://daisyui.com/components/badge/](https://daisyui.com/components/badge/)
///

## Installation

```bash
cotton-daisy add badge
```

## Usage

/// Tab | Basic

```html

<c-badge>Badge</c-badge>
```

///

/// Tab | Type

```html

<c-badge type="primary">Primary</c-badge>
<c-badge type="secondary">Secondary</c-badge>
<c-badge type="success">Success</c-badge>
<c-badge type="warning">Warning</c-badge>
<c-badge type="error">Error</c-badge>
```

///

/// Tab | Size

```html

<c-badge size="lg">Large</c-badge>
<c-badge size="md">Medium</c-badge>
<c-badge size="sm">Small</c-badge>
<c-badge size="xs">Extra Small</c-badge>
```

///

/// Tab | Outline

```html

<c-badge outline>Outline</c-badge>
```

///