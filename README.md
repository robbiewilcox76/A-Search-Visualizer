## NOTICE: HEAP Change

- MinHeap implements 2 tie-breakers: (represented by MinHeap.mode)
  - **default** mode = 1: favouring smaller g values if f values are equal
  - mode = 2: favouring larger g values if f values are equal

- If not set heap's mode, it always use **default**
- In order to change heap's mode, preset MinHeap.mode = {ModeNumber} before using. 