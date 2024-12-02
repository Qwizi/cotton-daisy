# Skeleton

| Argument       | Required               | Type     | Default | Description                                                                                   |
|----------------|------------------------|----------|---------|-----------------------------------------------------------------------------------------------|
| `h`            | Yes                    | `string` | `null`  | Specifies the height of the skeleton. Accepts numeric values as strings (e.g., `"32"`).       |
| `w`            | Yes                    | `string` | `null`  | Specifies the width of the skeleton. Accepts numeric values as strings (e.g., `"32"`).        |
| `rounded`      | No                     | `string` | `null`  | Adds rounded corners to the skeleton. Accepts CSS rounding values (e.g., `full`, `lg`, `md`). |
 /// admonition | Component from DaisyUI 

[https://daisyui.com/components/skeleton/](https://daisyui.com/components/skeleton/)
///

## Installation

```bash
cotton-daisy add skeleton
```

## Usage

/// Tab | Basic

```html

<div class="flex w-52 flex-col gap-4">
    <div class="flex items-center gap-4">
        <c-skeleton h="16" w="16" rounded="full"/>
        <div class="flex flex-col gap-4">
            <c-skeleton h="4" w="20"/>
            <c-skeleton h="4" w="20"/>
        </div>
    </div>
    <c-skeleton h="32" w="full"/>
</div>
```

///