# Menu

| Argument      | Required | Type      | Default     | Description                                                                                  |
|---------------|----------|-----------|-------------|----------------------------------------------------------------------------------------------|
| `bg`          | No       | `string`  | `"base-200"`| Specifies the background color of the menu. Options depend on your CSS (e.g., `primary`, `secondary`). |
| `w`           | No       | `string`  | `"56"`      | Specifies the width of the menu. Accepts numeric values or predefined CSS classes (e.g., `"56"`, `"full"`). |
| `size`        | No       | `string`  | `null`      | Specifies the size of the menu items. Options depend on your CSS (e.g., `"lg"`, `"sm"`).      |
| `title`       | No       | `string`  | `null`      | Adds a title to the menu. Displayed as a heading above the menu items.                       |
| `responsive`  | No       | `boolean` | `false`     | Makes the menu responsive. Adds `menu-vertical` for small screens and `menu-horizontal` for larger screens. |
| `horizontal`  | No       | `boolean` | `false`     | Makes the menu layout horizontal. Overrides `responsive` if both are used.                   |


/// admonition | Component from DaisyUI
[https://daisyui.com/components/menu/](https://daisyui.com/components/menu/)
///

## Installation

```bash
cotton-daisy add menu
```

## Usage

/// Tab | Basic

```html

<c-menu title="Menu Title">
    <li><a href="#home">Home</a></li>
    <li><a href="#about">About</a></li>
</c-menu>
```

///