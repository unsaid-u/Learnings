Concurrent Batch Processing 
If you want to process multiple batches concurrently instead of sequentially:

javascript
```
async function processInBatchesConcurrently(array, batchSize, processBatch) {
    const promises = [];
    for (let i = 0; i < array.length; i += batchSize) {
        const batch = array.slice(i, i + batchSize);
        promises.push(processBatch(batch));
    }
    await Promise.all(promises); // Wait for all batches to complete
}

```
