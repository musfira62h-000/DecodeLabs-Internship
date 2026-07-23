# Task 1 — The Global Launch (Cloud Computing Project 1)

Host a static portfolio website on cloud storage — **no servers** — with a public, shareable URL.

**Deliverable:** A live `https://` URL that opens Musfira Hassan's portfolio anywhere in the world.

## Live URL
Deployed on **Azure Blob Storage** (Static website):
```
https://musfiraportfolio2026.z13.web.core.windows.net/
```
> Replace with your exact **Primary endpoint** from Azure Portal → Storage account → Static website (the `z##` part is auto-assigned).

## Files in this folder

| File | Purpose |
|------|---------|
| `index.html` | The complete portfolio — **CSS is inlined**, so this one file is the whole site (index document). |
| `error.html` | Friendly 404 page (used as the error document). |
| `bucket-policy.json` | AWS S3 policy that makes objects publicly readable (only needed for the AWS path). |
| `README.md` | This guide. |

> **Self-contained:** `index.html` has all styling built in, so even if `error.html` isn't uploaded the site still works perfectly.

> Preview locally: double-click `index.html`, or run `python -m http.server 8000` in this folder and open `http://localhost:8000`.

---

## Option A — Azure Blob Storage (used for this deployment)

1. [Azure Portal](https://portal.azure.com) → **Storage accounts** → **Create** (StorageV2, LRS, an allowed region e.g. Central India).
2. Open the storage account → **Static website** (left menu) → **Enabled**.
   - **Index document name:** `index.html`
   - **Error document path:** `error.html`
   - **Save** → copy the **Primary endpoint** (`https://<name>.z##.web.core.windows.net/`) — this is your live link.
3. Static website creates a **`$web`** container. Go to **Containers → `$web` → Upload** and add `index.html` and `error.html`.
4. Open the **Primary endpoint** URL — your site is live over **https**.

Azure CLI alternative:
```bash
az storage blob service-properties update --account-name YOURACCOUNT \
  --static-website --index-document index.html --404-document error.html

az storage blob upload-batch -s . -d '$web' --account-name YOURACCOUNT \
  --pattern "*.html"
```

---

## Option B — AWS S3

### 1. Create the bucket
1. [S3 Console](https://console.aws.amazon.com/s3/) → **Create bucket**.
2. **Bucket name:** globally unique, e.g. `musfira-portfolio-2026`.
3. **Region:** e.g. `ap-south-1` (Mumbai).
4. **Block Public Access:** uncheck "Block all public access" + confirm.
5. **Create bucket**.

### 2. Upload
Bucket → **Upload** → add `index.html` and `error.html` → **Upload**.

### 3. Enable Static Website Hosting
Bucket → **Properties** → **Static website hosting** → **Edit** → **Enable**.
Index document `index.html`, Error document `error.html` → **Save**. Note the **Bucket website endpoint**.

### 4. Public bucket policy
Bucket → **Permissions** → **Bucket policy** → **Edit** → paste `bucket-policy.json`, replace `YOUR-BUCKET-NAME` → **Save**.

> Note: S3 website endpoints are `http://` by default. For `https://`, put **CloudFront** in front of the bucket (also adds global CDN speed).

### 5. Test
Open the endpoint:
```
http://musfira-portfolio-2026.s3-website.ap-south-1.amazonaws.com
```

AWS CLI alternative:
```bash
aws s3 cp index.html s3://YOUR-BUCKET-NAME/
aws s3 cp error.html s3://YOUR-BUCKET-NAME/
aws s3api put-bucket-policy --bucket YOUR-BUCKET-NAME --policy file://bucket-policy.json
aws s3 website s3://YOUR-BUCKET-NAME/ --index-document index.html --error-document error.html
```

---

## Submission checklist
- [x] Public storage account/bucket created
- [x] `index.html` and `error.html` uploaded
- [x] Static website hosting enabled (index + error documents set)
- [x] Public access configured
- [ ] Live URL opens the portfolio in an incognito window
- [ ] URL saved for submission

## Stretch goals (from the PDF conclusion)
- Configure a **custom domain**.
- Put a **CDN** in front (Azure CDN / AWS CloudFront) for global speed.
