# Modal

| Argument       | Required | Type      | Default | Description                                                                                                        |
|----------------|----------|-----------|---------|--------------------------------------------------------------------------------------------------------------------|
| `w`            | No       | `string`  | `null`  | Specifies the width of the modal. Accepts numeric values or predefined CSS classes (e.g., `"96"`, `"full"`, etc.). |
| `max_w`        | No       | `string`  | `null`  | Specifies the maximum width of the modal. Accepts numeric values or predefined CSS classes (e.g., `"md"`, `"lg"`). |
| `close_button` | No       | `boolean` | `true`  | Displays a close button in the top-right corner of the modal if set to `true`.                                     |
| `title`        | No       | `string`  | `null`  | Adds a title to the modal. Displayed at the top of the modal content.                                              |

/// admonition | Component from DaisyUI
[https://daisyui.com/components/modal/](https://daisyui.com/components/modal/)
///

## Installation

```bash
cotton-daisy add modal
```

## Usage

/// Tab | Basic

```html

<c-button onclick="my_modal.showModal()">Open modal</c-button>
<c-modal id="my_modal" title="Modal Title">
    <p>Modal content</p>
</c-modal>
```

///

/// Tab | Without close btn

```html

<c-button onclick="my_modal.showModal()">Open modal</c-button>
<c-modal id="my_modal" title="Modal Title" close_button="False">
    <p>Modal content</p>
</c-modal>
```

///