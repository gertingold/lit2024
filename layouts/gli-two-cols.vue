<!--
  Usage:
```md
---
layout: gli-two-cols
---
::left::
# Left
This shows on the left
::right::
# Right
This shows on the right
```
-->

<script setup lang="ts">
const props = defineProps({
  class: {
    type: String,
  },
  layoutClass: {
    type: String,
  },
})
</script>

<template>
  <div class="slidev-layout gli-two-cols w-full h-full" :class="layoutClass">
    <div class="col-left" :class="props.class">
      <slot name="left" />
    </div>
    <div class="col-right" :class="props.class">
      <slot name="right" />
    </div>
  </div>
</template>

<style scoped>
.gli-two-cols {
  display: grid;
  grid-column-gap: 20px;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 1fr;
}

.col-left {
  grid-area: 1 / 1 / 2 / 1;
}
.col-right {
  grid-area: 1 / 2 / 2 / 2;
}
</style>
