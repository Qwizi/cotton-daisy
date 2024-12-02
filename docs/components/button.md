# Button

| Argument       | Required | Type      | Default | Description                                                                            |
|----------------|----------|-----------|---------|----------------------------------------------------------------------------------------|
| `type`         | No       | `string`  | `null`  | Specifies the button style. Options depend on your CSS (e.g., `primary`, `secondary`). |
| `active`       | No       | `boolean` | `false` | Adds an active state to the button if set to `true`.                                   |
| `outline`      | No       | `boolean` | `false` | Adds an outline style to the button if set to `true`.                                  |
| `block`        | No       | `boolean` | `false` | Makes the button take the full width of its container if set to `true`.                |
| `size`         | No       | `string`  | `null`  | Specifies the size of the button. Options depend on your CSS (e.g., `lg`, `sm`).       |
| `wide`         | No       | `boolean` | `false` | Makes the button wider than the default width if set to `true`.                        |
| `square`       | No       | `boolean` | `false` | Makes the button a square shape if set to `true`.                                      |
| `circle`       | No       | `boolean` | `false` | Makes the button a circle shape if set to `true`.                                      |
| `join`         | No       | `boolean` | `false` | Adds `join-item` class for buttons that are grouped together in a "join" style.        |
| `no_animation` | No       | `boolean` | `false` | Disables animations for the button if set to `true`.                                   |

/// admonition | Component from DaisyUI
[https://daisyui.com/components/button/](https://daisyui.com/components/button/)
///

## Installation

```bash
cotton-daisy add button
```

## Usage

/// Tab | Basic

```html

<c-button>Button</c-button>
```

///

/// Tab | Type

```html

<c-button type="primary">Primary</c-button>
<c-button type="secondary">Secondary</c-button>
<c-button type="success">Success</c-button>
<c-button type="warning">Warning</c-button>
<c-button type="error">Error</c-button>
```

///

/// Tab | Size

```html

<c-button size="lg">Large</c-button>
<c-button size="md">Medium</c-button>
<c-button size="sm">Small</c-button>
<c-button size="xs">Extra Small</c-button>
```

///

/// Tab | Active

```html

<c-button active>Active</c-button>
```

///

/// Tab | Outline

```html

<c-button outline>Outline</c-button>
```

///

/// Tab | Block

```html

<c-button block>Block</c-button>
```

///

/// Tab | Wide

```html

<c-button wide>Wide</c-button>
```

///

/// Tab | Square

```html

<c-button square>Square</c-button>
```

///

/// Tab | Circle

```html

<c-button circle>Circle</c-button>
```

///

/// Tab | Join

```html

<div class="join">
    <c-button join>Join</c-button>
    <c-button join>Join</c-button>
    <c-button join>Join</c-button>
</div>
```

///

