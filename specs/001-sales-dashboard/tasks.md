# Tasks: ShopSmart Sales Analytics Dashboard

**Input**: Design documents from `specs/001-sales-dashboard/`
**Prerequisites**: spec.md (user stories), plan decisions (single `app.py`, no automated tests)

**Tests**: Not included — manual browser verification per the constitution (Principle V).

**Organization**: Tasks grouped by user story to enable independent implementation and
testing of each story. All code lives in a single `app.py` file.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US4)
- File paths are relative to repository root

---

## Phase 1: Setup

**Purpose**: Create the two project files needed before any feature work begins.

- [x] T001 Create `app.py` with a minimal Streamlit shell: import streamlit, set page title to "ShopSmart Sales Dashboard"
- [x] T002 [P] Create `requirements.txt` declaring streamlit, plotly, and pandas as dependencies

**Checkpoint**: Repository has `app.py` and `requirements.txt`; `streamlit run app.py` launches a blank page.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Page-level configuration shared by all user stories.

**⚠️ CRITICAL**: All user story work depends on this phase being complete.

- [x] T003 Configure Streamlit page settings in `app.py`: wide layout mode, browser tab title "ShopSmart Sales Dashboard", and a visible `st.title` header

**Checkpoint**: Foundation ready — `streamlit run app.py` shows the branded header in wide layout.

---

## Phase 3: User Story 1 — KPI Overview (Priority: P1) 🎯 MVP

**Goal**: Display Total Sales and Total Orders as formatted metric cards.

**Independent Test**: Load the dashboard and confirm two KPI cards are visible with values
matching manual calculations from `data/sales-data.csv`.

### Implementation for User Story 1

- [x] T004 [US1] Load `data/sales-data.csv` into a pandas DataFrame in `app.py` (read CSV, parse `date` column as datetime)
- [x] T005 [US1] Compute Total Sales (sum of `total_amount`) and Total Orders (row count) from the DataFrame in `app.py`
- [x] T006 [US1] Render two `st.metric` KPI cards in `app.py`: Total Sales formatted as currency (e.g. $682,450) and Total Orders with comma separators

**Checkpoint**: User Story 1 fully functional — KPI cards display correct values from CSV.

---

## Phase 4: User Story 2 — Sales Trend Chart (Priority: P2)

**Goal**: Line chart showing monthly aggregated sales across all 12 months.

**Independent Test**: Verify the chart shows one data point per month, the monthly values
sum to the Total Sales KPI, and tooltips show exact amounts on hover.

### Implementation for User Story 2

- [ ] T007 [US2] Aggregate the DataFrame by month in `app.py`: group by year-month, sum `total_amount`, sort chronologically
- [ ] T008 [US2] Render a Plotly line chart of monthly sales in `app.py` with labelled axes and interactive hover tooltips showing month and exact sales amount

**Checkpoint**: User Stories 1 and 2 both independently functional.

---

## Phase 5: User Story 3 — Category & Region Breakdowns (Priority: P3)

**Goal**: Two sorted bar charts — sales by category and sales by region — displayed
side by side on wide screens and stacked on narrow screens.

**Independent Test**: Verify both charts show all categories/regions sorted highest to
lowest, tooltips work, and layout responds to viewport width.

### Implementation for User Story 3

- [ ] T009 [US3] Render a Plotly bar chart of sales by product category in `app.py`: group DataFrame by `category`, sum `total_amount`, sort descending, add hover tooltips
- [ ] T010 [US3] Render a Plotly bar chart of sales by geographic region in `app.py`: group DataFrame by `region`, sum `total_amount`, sort descending, add hover tooltips
- [ ] T011 [US3] Wrap category and region charts in `st.columns(2)` in `app.py` so they appear side by side on wide viewports; Streamlit's responsive behaviour handles narrow screens automatically

**Checkpoint**: All three user stories independently functional.

---

## Phase 6: User Story 4 — Graceful Data Validation (Priority: P4)

**Goal**: Validate CSV on load; show sidebar warnings for issues without crashing
unaffected sections.

**Independent Test**: Load the dashboard with a deliberately malformed CSV and confirm
the sidebar warning appears while KPI cards and charts that can still compute do render.

### Implementation for User Story 4

- [ ] T012 [US4] Add a CSV validation function in `app.py` that checks for the 8 required columns (`date`, `order_id`, `product`, `category`, `region`, `quantity`, `unit_price`, `total_amount`) and collects a list of warning messages
- [ ] T013 [US4] Add a missing-file guard in `app.py`: if `data/sales-data.csv` does not exist, display a descriptive `st.error` message and `st.stop()` to halt rendering
- [ ] T014 [US4] Render a collapsible `st.sidebar.expander("⚠️ Data Warnings")` in `app.py` that lists all collected validation warnings; only show the expander when warnings exist

**Checkpoint**: All four user stories independently functional; dashboard degrades gracefully.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Branding, final dependency check, and deployment.

- [ ] T015 Apply ShopSmart accent color to all Plotly charts and KPI card styling in `app.py` (use a consistent blue/teal hex value via Plotly `color_discrete_sequence` and `st.markdown` CSS)
- [ ] T016 Review and finalize `requirements.txt`: confirm all imported packages are listed and versions are compatible with Streamlit Community Cloud
- [ ] T017 Deploy to Streamlit Community Cloud via the web UI: connect the GitHub repo, set main file to `app.py`, verify the live public URL renders all four sections correctly

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately; T001 and T002 can run in parallel
- **Foundational (Phase 2)**: Depends on Phase 1 — blocks all user stories
- **User Story 1 (Phase 3)**: Depends on Phase 2
- **User Story 2 (Phase 4)**: Depends on Phase 3 (needs the loaded DataFrame)
- **User Story 3 (Phase 5)**: Depends on Phase 3 (needs the loaded DataFrame)
- **User Story 4 (Phase 6)**: Depends on Phase 3 (wraps the CSV loading already established)
- **Polish (Phase 7)**: Depends on all user story phases complete

### User Story Dependencies

- **US1 (P1)**: Starts after Phase 2 — no dependency on other stories
- **US2 (P2)**: Depends on US1 (reuses the loaded DataFrame from T004)
- **US3 (P3)**: Depends on US1 (reuses the loaded DataFrame from T004); independent of US2
- **US4 (P4)**: Depends on US1 (wraps the CSV load from T004 with validation)

### Parallel Opportunities

- T001 and T002 (Setup) can run in parallel — different files
- US2 (Phase 4) and US3 (Phase 5) can run in parallel after US1 is complete — no inter-story dependencies

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (KPI cards)
4. **STOP and VALIDATE**: Confirm KPI values match CSV calculations
5. Deploy if ready

### Incremental Delivery

1. Setup + Foundational → blank branded page
2. Add US1 → KPI cards visible (**MVP**)
3. Add US2 → trend chart added
4. Add US3 → breakdown charts added
5. Add US4 → validation and error handling added
6. Polish + Deploy → live public URL

---

## Notes

- All 17 tasks touch `app.py`; no parallel execution within a phase (single file)
- T001 and T002 are the only parallel pair (different files)
- US2 and US3 can be developed in parallel by different people after US1 is complete
- Manual browser verification is the only required testing (per constitution Principle V)
- Accent color hex value for T015 is a decision for the implementer (blue/teal assumed)
