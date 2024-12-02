# Divider

| Argument     | Required | Type      | Default   | Description                                                                                   |
|--------------|----------|-----------|-----------|-----------------------------------------------------------------------------------------------|
| `type`       | No       | `string`  | `null`    | Specifies the type of the divider. Options depend on your CSS (e.g., `primary`, `secondary`). |
| `position`   | No       | `string`  | `default` | Positions the divider. [`start`, `end`].                                                      |
| `horizontal` | No       | `boolean` | `false`   | Makes the divider horizontal if set to `true`.                                                |

/// admonition | Component from DaisyUI
[https://daisyui.com/components/divider/](https://daisyui.com/components/divider/)
///

## Installation

```bash
cotton-daisy add divider
```

## Usage

/// Tab | Basic

```html

<c-divider/>
```

///

/// Tab | Type

```html

<c-divider type="primary"/>
<c-divider type="secondary"/>
<c-divider type="success"/>
<c-divider type="warning"/>
<c-divider type="error"/>
```

///

/// Tab | Position

```html

<c-divider position="start">Start</c-divider>
<c-divider>Default</c-divider>
<c-divider position="end">End</c-divider>
```

///

/// Tab | Horizontal

```html

<c-divider horizontal/>
```

///
