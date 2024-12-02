# Card

| Argument     | Required | Type      | Default                    | Description                                                                                            |
|--------------|----------|-----------|----------------------------|--------------------------------------------------------------------------------------------------------|
| `bg`         | No       | `string`  | `"base-100"`               | Specifies the background color of the card. Options depend on your CSS (e.g., `primary`, `secondary`). |
| `w`          | No       | `string`  | `"96"`                     | Specifies the width of the card. Accepts numeric values as strings (e.g., `"96"`, `"full"`, etc.).     |
| `title`      | No       | `string`  | `null`                     | Adds a title to the card. Displayed as a heading inside the card.                                      |
| `shadow`     | No       | `string`  | `null`                     | Applies a shadow to the card. Options depend on your CSS (e.g., `sm`, `lg`).                           |
| `compact`    | No       | `boolean` | `false`                    | Enables a compact style for the card.                                                                  |
| `image_full` | No       | `boolean` | `false`                    | Enables a full-sized image layout for the card.                                                        |
| `glass`      | No       | `boolean` | `false`                    | Applies a glass effect to the card background.                                                         |
| `side`       | No       | `boolean` | `false`                    | Arranges the card in a side-by-side layout when set to `true`.                                         |
| `image_src`  | No       | `string`  | `null`                     | Specifies the source URL for the card's image.                                                         |
| `image_alt`  | No       | `string`  | `"Image alternative text"` | Specifies the alt text for the card's image.                                                           |

/// admonition | Component from DaisyUI
[https://daisyui.com/components/card/](https://daisyui.com/components/card/)
///

## Installation

```bash
cotton-daisy add card
```

## Usage

/// Tab | Basic

```html

<c-card title="Card Title" description="Card description"/>
```

///

/// Tab | Custom content

```html

<c-card>
    <div class="flex flex-col gap-4">
        <h2 class="text-lg font-semibold">Card Title</h2>
        <p class="text-sm">Card description</p>
    </div>
</c-card>
```

///

/// Tab | Footer

```html

<c-card title="Card Title" description="Card description">
    <c-slot name="footer">
        <button class="btn btn-primary">Action</button>
    </c-slot>
</c-card>
```

///

/// Tab | With Image

```html

<c-card
        title="Card Title"
        description="Card description"
        image_src="https://via.placeholder.com/150"
        image_alt="Placeholder image"
/>
```

///

/// Tab | Compact

```html

<c-card title="Card Title" description="Card description" compact/>
```

///

/// Tab | Glass

```html

<c-card title="Card Title" description="Card description" glass/>
```

///

/// Tab | Side

```html

<c-card title="Card Title" description="Card description" side/>
```

///

/// Tab | With Image Full

```html

<c-card
        title="Card Title"
        description="Card description"
        image_src="https://via.placeholder.com/150"
        image_alt="Placeholder image"
        image_full
/>
```

///