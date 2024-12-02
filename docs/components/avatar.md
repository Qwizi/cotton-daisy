# Avatar

| Argument        | Required | Type      | Default | Description                                                                                     |
|-----------------|----------|-----------|---------|-------------------------------------------------------------------------------------------------|
| `w`             | No       | `string`  | `16`    | Specifies the width of the avatar. Accepts numeric values as strings (e.g., `"16"`).            |
| `online_status` | No       | `boolean` | `false` | Determines if the online/offline status indicator is displayed.                                 |
| `online`        | No       | `boolean` | `false` | Indicates whether the user is online. Used with `online_status`.                                |
| `offline`       | No       | `boolean` | `false` | Indicates whether the user is offline. Overrides `online` if both are provided.                 |
| `rounded`       | No       | `boolean` | `false` | Makes the avatar rounded. Can accept additional classes (e.g., `"full"`, `"lg"`, `"md"`, etc.). |
| `src`           | Yes      | `string`  | `null`  | The URL of the avatar image.                                                                    |
| `alt`           | Yes      | `string`  | `null`  | Alternative text for the avatar image.                                                          |

/// admonition | Component from DaisyUI
[https://daisyui.com/components/avatar/](https://daisyui.com/components/avatar/)
///

## Installation

```bash
cotton-daisy add avatar
```

## Usage

/// tab | Basic
```html
<c-avatar
        src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
        alt="User avatar"
/>
```
///

/// tab | Online Status
```html
<c-avatar
        online_status
        online
        src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
        alt="User avatar"
/>
```
///

/// tab | Offline Status
```html
<c-avatar
        online_status
        online="False"
        src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
        alt="User avatar"
/>
```
///

/// tab | Rounded
```html
<c-avatar
        rounded="full"
        src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
        alt="User avatar"
/>
```
///

/// tab | Custom Width
```html
<c-avatar
        w="24"
        src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
        alt="User avatar"
/>
```
///


